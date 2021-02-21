# 02. Email Vlidator

class NameTooShortError(Exception):
	""" Raised when username is 4 symbols or less """
	pass
	

class MustContainAtSymbolError(Exception):
	""" Raised when the email is missing @"""
	pass
	

class InvalidDomainError(Exception):
	""" Raised when the domain of the email is invalid """
	pass


def validate_name(email):
	username = email.split("@")[0]
	if len(username) <= 4:
		raise NameTooShortError("Name must be more than 4 characters")
		

def validate_at_symbol(email):
	if "@" not in email:
		raise MustContainAtSymbolError("Email must contain @")
		
		
def validate_domain(email, valid_domains):
	domain = email.split(".")[-1]
	if domain not in valid_domains:
		raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
	

while True:
	line = input()
	valid_domains = ("com", "net", "bg", "org")
	if line == "End":
		break
		
	validate_name(line)
	validate_at_symbol(line)
	validate_domain(line, valid_domains)
	
	print("Email is valid")




















