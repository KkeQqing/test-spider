#version
beautifulsoup4             4.13.5   
python                     3.13.7     
requests                   2.32.5    


将 environment.yml 文件放在项目根目录，然后在anaconda prompt运行：  
conda env create -f environment.yml  
Conda 会：  
读取文件中的 name 作为环境名  
安装指定的 Python 版本  
安装所有列出的包  