import pathlib
import shutil
import subprocess

import myConfig

myConfig.load_config('conf_local.yaml')
TEMP_PATH = myConfig.get_config("docu", "temp_path")
DOCU_PATH = pathlib.PurePath(myConfig.get_project_root_path(), myConfig.get_config('docu', 'html_source_path'))
ZIP_FILENAME = pathlib.PurePath(myConfig.get_config("docu", "temp_path"), 'html')
ARTIFACTORY_CREDENTIALS = myConfig.get_config("docu", "artifactory-credentials")
ARTIFACTORY_PATH = myConfig.get_config("docu", "artifactory-path")
JENKINS_CREDENTIALS = myConfig.get_config("docu", "jenkins-credentials")
JENKINS_JOB = myConfig.get_config("docu", "jenkins-job")


def zip_docu():
    print(f'Zipping {DOCU_PATH} to {ZIP_FILENAME}')

    shutil.make_archive(str(ZIP_FILENAME), format='zip', root_dir=str(DOCU_PATH))


def upload_docu_to_artifactory():
    # noinspection SpellCheckingInspection
    cmd_str = fr'curl -X PUT --user {ARTIFACTORY_CREDENTIALS} --output nul --data-binary @{ZIP_FILENAME}.zip {ARTIFACTORY_PATH}'
    print(f'Uploading to artifactory: {cmd_str}')

    subprocess.run(cmd_str, cwd=TEMP_PATH, shell=True)


def copy_to_doku_server():
    cmd_str = fr'curl -X POST --user {JENKINS_CREDENTIALS} {JENKINS_JOB}'
    print(f'Copying to doku server: {cmd_str}')

    subprocess.run(cmd_str, cwd=TEMP_PATH, shell=True)


def update_docu_on_vdoc():
    zip_docu()
    upload_docu_to_artifactory()
    copy_to_doku_server()


if __name__ == '__main__':
    update_docu_on_vdoc()