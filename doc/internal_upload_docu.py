
import pathlib
import shutil
import subprocess
import yaml

_config: dict | None = None


def get_project_root_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent


def load_config(yaml_file_name: str):
    with open(pathlib.PurePath(get_project_root_path(), "configuration/" + yaml_file_name)) as yaml_file:
        config_dict = yaml.safe_load(yaml_file)

    global _config
    _config = config_dict

def get_config(level1_key: str, level2_key: str | None = None) -> str:
    global _config
    try:
        if level2_key is None:
            return _config[level1_key]
        else:
            return _config[level1_key][level2_key]
    except KeyError:
        raise KeyError(f"Configuration for ['{level1_key}']['{level2_key}'] not found!")


def zip_docu():
    docu_path = pathlib.PurePath(get_project_root_path(), get_config('docu', 'html_source_path'))
    zip_filename = pathlib.PurePath(get_config("docu", "temp_path"), 'html')

    print(f'Zipping {docu_path} to {zip_filename}')
    shutil.make_archive(str(zip_filename), format='zip', root_dir=str(docu_path))


def upload_docu_to_artifactory():
    artifactory_credentials = get_config("docu", "artifactory-credentials")
    temp_path = get_config("docu", "temp_path")
    zip_filename = pathlib.PurePath(get_config("docu", "temp_path"), 'html')
    artifactory_path = get_config("docu", "artifactory-path")

    # noinspection SpellCheckingInspection
    cmd_str = fr'curl -X PUT --user {artifactory_credentials} --output nul --data-binary @{zip_filename}.zip {artifactory_path}'
    print(f'Uploading to artifactory: {cmd_str}')

    subprocess.run(cmd_str, cwd=temp_path, shell=True)


def copy_to_doku_server():
    cmd_str = fr'curl -X POST --user {get_config("docu", "jenkins-credentials")} {get_config("docu", "jenkins-job")}'
    print(f'Copying to doku server: {cmd_str}')

    subprocess.run(cmd_str, cwd=get_config("docu", "temp_path"), shell=True)


def update_docu_on_vdoc():
    zip_docu()
    upload_docu_to_artifactory()
    copy_to_doku_server()


if __name__ == '__main__':
    load_config('conf_local.yaml')
    update_docu_on_vdoc()