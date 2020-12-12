import os
import cv2
from app.service.module_service import return_output
from app.const.const import Const

def get_test(input_value):
    print(f'Moudule::get_test, input_value={input_value}')
    output_value = return_output(input_value)
    
    return dict(
        input_value=input_value,
        output_value=output_value
    )