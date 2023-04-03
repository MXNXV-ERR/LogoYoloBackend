from rest_framework.response import Response
from rest_framework.decorators import api_view
from .code import pickleissour,tensorcaller,imglogo


@api_view(['POST'])
def getPredPickelReview(request):
    review = request.data['input_text']
    pred=pickleissour.getJoblibModelPred(review)
    ret={"pred":pred}
    return Response(ret)


@api_view(['POST'])
def getPredTensorReview(request):
    review = request.data['input_text']
    pred=tensorcaller.getTensorModelPred(review)
    ret={"pred":pred}
    return Response(ret)


@api_view(['POST'])
def getImagePred(request):
    img_data=request.data['img']
    ret = imglogo.getImgPred(img_data)
    return Response(ret)
