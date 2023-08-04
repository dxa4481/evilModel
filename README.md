# Evil Model
The Llama/llama2 models available for download by facebook are pytorch files, which can be malicious files.

This is because they're pickle files, which can contain arbitrary Python code inside them. 

This repo has an example evil ML model, that creates a file on your filesystem.

You can run it with the following:

create the pytorch file:
```bash
python evil.py
```

run the pytorch file:
```bash
torchrun --nproc_per_node 1 loader.py
```

Note the "loader.py" file here is actually non-malicious, the only malicious file is the .pth file, which is the same format llama uses.
