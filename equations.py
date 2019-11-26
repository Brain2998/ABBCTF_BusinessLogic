import numpy
import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def getRandInt():
    return random.randint(-1000,1000)

def generateSystem():
    #Generates system of 3 linear equations

    #generate solutions x,y,z
    solutions=[getRandInt(), getRandInt(), getRandInt()]
    #generate coefficients a,b,c
    coeffecients=[[getRandInt(), getRandInt(), getRandInt()], [getRandInt(), getRandInt(), getRandInt()], [getRandInt(), getRandInt(), getRandInt()]]
    #calculate results d
    results=[solutions[0]*coeffecients[0][0]+solutions[1]*coeffecients[0][1]+solutions[2]*coeffecients[0][2], solutions[0]*coeffecients[1][0]+solutions[1]*coeffecients[1][1]+solutions[2]*coeffecients[1][2], solutions[0]*coeffecients[2][0]+solutions[1]*coeffecients[2][1]+solutions[2]*coeffecients[2][2]]
    #check does system has only one solution
    try:
        numpy.linalg.solve(numpy.array(coeffecients),numpy.array(results))
        return {'solutions': solutions, 'coeffecients':coeffecients, 'results': results}
    except numpy.linalg.LinAlgError:
    #otherwise generate new system
        generateSystem()

def createSystemImageFromText(system):
    #Creates image representation of system of linear equations
    img=Image.new('RGB', (900, 200))
    drawer=ImageDraw.Draw(img)
    font=ImageFont.truetype('static/HanaleiFill-Regular.ttf', 55)
    drawer.text((0,0), system, font=font)
    byteArr=BytesIO()
    img.save(byteArr, 'PNG')
    return byteArr.getvalue()

def createSystemTextFromDict(system):
    #Creates system representation in text like
    #a1*x+b1*y+c1*z=d1
    #a2*x+b2*y+c2*z=d2
    #a3*x+b3*y+c3*z=d3
    text='''{}x + {}y + {}z = {} 
{}x + {}y + {}z = {} 
{}x + {}y + {}z = {} '''.format(system['coeffecients'][0][0], system['coeffecients'][0][1], system['coeffecients'][0][2], system['results'][0],
    system['coeffecients'][1][0], system['coeffecients'][1][1], system['coeffecients'][1][2], system['results'][1],
    system['coeffecients'][2][0], system['coeffecients'][2][1], system['coeffecients'][2][2], system['results'][2])
    return text

#Tests
#generateSystem()
#print(createSystemTextFromDict(generateSystem()))
#createSystemImageFromText(createSystemTextFromDict(generateSystem()))
