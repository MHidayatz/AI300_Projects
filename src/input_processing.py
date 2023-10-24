def format_model_inputs(input_dict):
    contract_type = int(input_dict['Contract Type'])
    sex = input_dict['sex']
    bmi = float(input_dict['bmi'])
    children = int(input_dict['children'])
    smoker = input_dict['smoker']
    region = input_dict['region']

    return [contract_type, sex, bmi, children, smoker, region]