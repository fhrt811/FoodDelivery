import os
import sys
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# Configure Data Transformation
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

#Create a class for Data Transformation
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['Weather_conditions',
                                'Road_traffic_density', 'City']
            numerical_cols = ['Delivery_person_Age', 'Delivery_person_Ratings',
                              'Vehicle_condition', 'multiple_deliveries', 'distance']
            
            # Define the custom ranking for each ordinal variable
            Weather_conditions_categories = ['Sunny','Cloudy','Windy','Sandstorms','Stormy','Fog']
            Road_traffic_density_categories = ['Low', 'Medium', 'High', 'Jam']
            City_categories = ['Semi-Urban','Urban','Metropolitian']
            
            logging.info('Pipeline initiated')
            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            #Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[Weather_conditions_categories,Road_traffic_density_categories,City_categories])),
                    ('scaler', StandardScaler())
                ]
            )
            # Combining both the pipelines
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            logging.info('Pipeline completed')
            return preprocessor

        except Exception as e:
            logging.info('Exception occured in Data Transformation')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading Train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('reading train and test data completed')
            logging.info(f'Train DataFram Head : \n{train_df.head().to_string()}')
            logging.info(f'Test DataFrame Head : \n{test_df.head().to_string()}')
            logging.info('Obtaining Preprocessor object')

            preprocessing_obj = self.get_data_transformation_object()

            #Creating and dropping the Dependent and independent features
            target_column_name = 'Time_taken (min)'

            # dropping two slightly correlated columns along with target
            drop_columns = [target_column_name,
                            'Type_of_order', 'time_diff_minutes']
            
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df
            target_feature_test_df = test_df[target_column_name]

            #Transformation using preprocessor object

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info(
                "Applying preprocessing object on training and testing datasets.")
            
            # converting data in array to load array quickly
            # numpy array are superfast for ML
            train_arr = np.c_[input_feature_train_arr,
                              np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]

            # saving pickle file from preprocessor object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            logging.info('Error occured in initiate_data_transformation')
            raise CustomException(e,sys)