# Terminal_ChatGPT
Interact with ChatGPT through terminal.

# Requirements
Create an environment and Install openai library:

1. `conda create --name chat python=3.8`
2. `conda activate chat`
3. `pip install openai`

# Terminal Alias

If you want to launch the program with an alias create a new script named "chat.sh" in your ~/home directory with the following contents:

```
eval "$(conda shell.bash hook)"
conda activate chat
python ~/<PATH_TO_REPO>/chat.py
conda deactivate
```

Then add the following line to ~/home/.aliases:

`alias chat="~/./chat.sh"`

# Usage
Launch your terminal and just type 'chat' to interact with chatGPT!
Type 'exit' to end the conversation.

Note: Each consecutive turn feeds the api with the dialogue history so far, so the price builds up.
