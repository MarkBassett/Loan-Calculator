# don't modify the variable below, please
import argparse

parser = argparse.ArgumentParser()
parser.add_aurgument("--print_answer", action="store_true")
alphabet = input()
print(alphabet[14])