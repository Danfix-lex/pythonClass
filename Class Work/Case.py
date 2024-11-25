announcement = """Investigation: 
1: don't lie did you use the toilet without flushing:
2: for did you use the toilet and flushed:\n"""

options = int(input(announcement))
match options:
	case 1:
		print("Thanks for speaking the truth.")
	case 2:
		print("Just hope that when the investigation is over, that you are not the one.")
	case _:
		print("investigation is still ongoing...")
