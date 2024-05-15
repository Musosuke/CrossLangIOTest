import os

function_name = "TestGenerator"
language_ext = {
    'python': '.py',
    'cpp': '.cpp',
}

input_params = [
    'dets',
    'tracks',
]
output_rtn_params = [
    'dx',
    'dy',
]

info_dict = {
    'function_name': function_name,
    'language_ext': language_ext,
    'input_params': input_params,
    'output_rtn_params': output_rtn_params,

    'rnd_input_generator': '_gnr_rnd_input.py',
    'result_comparator': '_Result_Compare.py',
}



def create_file(directory, filename):
    """Helper function to create an empty file in the specified directory."""
    with open(os.path.join(directory, filename), 'w') as f:
        f.write('')

# Make a directory named function_name
try:
    os.mkdir(function_name)
except FileExistsError:
    print("Directory already exists")

# Create necessary files
create_file(function_name, info_dict["rnd_input_generator"])
create_file(function_name, info_dict["result_comparator"])

# Create UnitTest files for each language extension
for ext in info_dict['language_ext'].values():
    create_file(function_name, f'_UnitTest{ext}')

# Create a config.txt file and write input and output parameters
with open(os.path.join(function_name, '_config.txt'), 'w') as f:
    # Write input parameters
    for param in info_dict['input_params']:
        file_name = f'Input_{param}.txt'
        f.write(file_name + '\n')

    f.write('\n')

    # Write output parameters
    for param in info_dict['output_rtn_params']:
        for language, ext in info_dict['language_ext'].items():
            file_name = f'Output_{language}_{param}.txt'
            f.write(file_name + '\n')
