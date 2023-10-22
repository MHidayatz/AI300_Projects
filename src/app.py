from flask import Flask, request, render_template
from model import Model
from input_processing import format_model_inputs

app = Flask(__name__)
