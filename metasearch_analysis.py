# coding: utf-8
#get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git)
#Path('data_not_in_repo').mkdir()
#get_ipython().magic('mv metasearch data_not_in_repo/')
from pathlib import Path
metasearch_dir = Path('data_not_in_repo/metasearch/')
data_exists = metasearch_dir.exists()
in_repro_course = Path.cwd().name == 'repro_course'
if data_exists and in_repro_course:
    print('data has been downloaded')
else:
    print('data has been downloaded or wrong directory')
