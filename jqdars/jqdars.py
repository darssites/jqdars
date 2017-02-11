class JQuery:

	jquery = ""

	def __init__(self, version="latest"):
		self.jquery = version

	def getRaw(self):
		return "<script src=\"http://code.jquery.com/jquery-{}.min.js\"></script>".format(self.jquery)