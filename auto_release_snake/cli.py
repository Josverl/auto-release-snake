

def snake_old():
    """
    This function returns a string that represents a blue snake in ASCII art.
    """
    return (
        "\033[34m"
        "         __\n"
        "        / _)\n"
        "   _.--._( (_\n"
        "  /  _   \\__)\n"
        " /  (_) _  \\\n"
        " \\_/\\___/\\_/\n"
        "\033[0m" 
    )

def snake():
    snake_say("Hello, I am not a cow.")
    

def snake_say(message):
    """
    Prints a message as if the snake is saying it, similar to cowsay.
    """
    # Prepare the speech bubble
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    top = ' ' + '_' * (max_length + 2)
    bottom = ' ' + '-' * (max_length + 2)
    bubble = [top]
    for line in lines:
        bubble.append(f"< {line.ljust(max_length)} >")
    bubble.append(bottom)
    # Print the bubble and the snake
    print('\n'.join(bubble))


if __name__ == "__main__":

    snake_say("Hello, I am not a cow.")
    