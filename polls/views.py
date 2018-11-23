from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Kaptiche is an enterprise data capture solution that enables organizations of all sizes to transform any documents into actionable information no matter how they are receivedIt is a comprehensive software that automates data capture, document classification, and indexing. The software consists of ready to use components for background processing and archiving system for easy integrations. This is simple to setup, quickly deployable, secure to run on any legacy systems and also it seamlessly integrates with a wide range of CRMs, BPMs & ERPs like SAP, Oracle, Microsoft Dynamics and more. Kaptiche is a browser-based application that can be hosted on your on-premise or on cloud in a highly secured manner.Kaptiche workflow begins with importing documents and ends with exporting meaningful data to downstream applications with the help of “Designed for Happiness” user interface. It provides a solution to improve productivity and reduces manual error/cost...")



def detail(request, question_id):
    return HttpResponse("You're looking at the results of question%s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResSponse("You're voting on question %s." % question_id)