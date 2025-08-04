# Create README
echo "# Market Making Strategy Simulator" > README.md

# Create requirements file
echo "numpy==1.23.5
pandas==1.5.3
matplotlib==3.7.0
requests==2.28.2
jupyter==1.0.0" > requirements.txt

# Create gitignore
echo "__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.ipynb_checkpoints
*.ipynb
.DS_Store
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/" > .gitignore