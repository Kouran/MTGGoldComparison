from flask import request

def extract_parameter(request, param_name):
	if request.args.get(param_name):
		return request.args.get(param_name)
	return ""

def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
