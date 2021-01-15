import argparse
from insulter import insulter 
from words import lookup
from number import number_trivia, get_date
def main():
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument("-i", "--insult", nargs="?", const="Alex", help="Custom insults, from God. (FOAAS API)")
  arg_parser.add_argument("-n", "--number", nargs=1, metavar="number", help="Number factoids")
  arg_parser.add_argument("-d", "--date", nargs=2, metavar=("month", "day"), help="Date Trivia")

  args = arg_parser.parse_args()

  if args.insult:
    insulter(args.insult)

  if args.number:
    number_trivia(str(args.number[0]))
      
  if args.date:
    get_date(str(args.date[0]), str(args.date[1]))

if __name__ == '__main__':
    main()