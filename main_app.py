import os
from sanic import Sanic, response
from sanic.exceptions import NotFound, SanicException
from lxml import etree

app = Sanic(__name__)

@app.route('/v1/give/<num>/fucks', methods=['GET','OPTIONS'])
async def give_fucks(request, num):
    accept_header_value = request.headers.get('Accept','application/json')
    response_mime_type = select_return_type(accept_header_value, ['application/json', 'application/xml'])

    try:
        num_asint = int(num)
    except ValueError:
        return error_response('What the fuck kind of number is {}?'.format(num), response_mime_type=response_mime_type)

    if request.method=='OPTIONS':
        return response.raw(b'',
                headers={'Allow': 'GET, OPTIONS',
                    'Content-Type': response_mime_type})

    if num_asint>=1000:
        return error_response('No one has that many fucking fucks to give.', status_code=410, response_mime_type=response_mime_type)
    elif num_asint>20:
        return error_response("Sorry, that's just too many fucks to give.", status_code=410, response_mime_type=response_mime_type)
    else:
        return fucks_given_response(num_asint, response_mime_type=response_mime_type)

@app.exception(NotFound)
async def not_found(request, exception):
    accept_header_value = request.headers.get('Accept','application/json')
    response_mime_type = select_return_type(accept_header_value, ['application/json', 'application/xml'])
   
    return error_response('What the fucking fuck are you looking for?',
            status_code=404,
            response_mime_type=response_mime_type)

@app.exception(SanicException)
async def other_error(request, exception):
    accept_header_value = request.headers.get('Accept','application/json')
    response_mime_type = select_return_type(accept_header_value, ['application/json', 'application/xml'])

    return error_response(exception.args[0],
            status_code=exception.status_code,
            response_mime_type=response_mime_type)
    
@app.middleware('response')
async def enable_cors(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization, User-Agent, X-Api-Key'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

@app.middleware('response')
async def set_servername(request, response):
    response.headers['Server'] = 'fuckservice/1.0'

def fucks_given_response(number_of_fucks, response_mime_type='application/json'):
    if response_mime_type=='application/json':
        retval = response.json({
            'status': 'ok',
            'fucks': ['fuck']*number_of_fucks
            },
            status=200)
    elif response_mime_type=='application/xml':
        nsmap = {None: 'http://faas.unnecessary.tech/schema'}

        root = etree.Element('{http://faas.unnecessary.tech/schema}ListOfFucks', nsmap=nsmap)
        status = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}status')
        status.text = 'ok'
        fucks = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}fucks')
        for i in range(number_of_fucks):
            a_fuck = etree.SubElement(fucks, '{http://faas.unnecessary.tech/schema}item')
            a_fuck.text = 'fuck'
        observation = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}observation')
        observation.text = 'Why the fuck are you still using XML?'

        retval = response.raw(etree.tostring(root, encoding='UTF-8', xml_declaration=True),
                headers={'Content-Type': 'application/xml'},
                status=200)

    else:
        retval = error_response('What fucking mime type do you want for your reponse?')

    return retval

def error_response(error_message, status_code=500, response_mime_type='application/json'):
    if response_mime_type=='application/json':
        retval = response.json({
            'status': 'error',
            'message': error_message
            },
            status=status_code)
    elif response_mime_type=='application/xml':
        nsmap = {None: 'http://faas.unnecessary.tech/schema'}

        root = etree.Element('{http://faas.unnecessary.tech/schema}Error', nsmap=nsmap)
        status = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}status')
        status.text = 'error'
        message = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}message')
        message.text = error_message

        observation = etree.SubElement(root, '{http://faas.unnecessary.tech/schema}observation')
        observation.text = 'Why the fuck are you still using XML?'

        retval = response.raw(etree.tostring(root, encoding='UTF-8', xml_declaration=True),
                headers={'Content-Type': 'application/xml'},
                status=status_code)
    else:
        retval = error_response('What fucking mime type do you want for your reponse?')

    return retval

def parse_accept_header(accept_header_value):
    components = accept_header_value.split(',')
    accept_values = []
    for c in components:
        if ';' in c:
            subcomponents = [t.strip() for t in c.split(';')]
            mime_type = subcomponents[0]
            for modifier in subcomponents[1:]:
                if modifier.startswith('q='):
                    weight_value = float(modifier[2:])
                    break
            else:
                weight_value = 1.0

            accept_values.append((weight_value, mime_type))
        else:
            accept_values.append((1.0, c.strip()))

    accept_values.sort(reverse=True)

    return accept_values

def select_return_type(accept_header_value, response_content_types):
    weighted_accept_values = parse_accept_header(accept_header_value)

    return_values = []

    for content_type in response_content_types:
        content_base, content_subtype = content_type.split('/')

        for weight, accept_type in weighted_accept_values:
            accept_base, accept_subtype = accept_type.split('/')

            if accept_base=='*' and accept_subtype=='*':
                return_values.append((weight, content_type))
            elif accept_base==content_base and accept_subtype=='*':
                return_values.append((weight, content_type))
            elif accept_base==content_base and accept_subtype==content_subtype:
                return_values.append((weight, content_type))

    return_values.sort(key=lambda x: x[0], reverse=True)

    if len(return_values)>0:
        result = return_values[0][1]
    else:
        result = None

    return result

if __name__=='__main__':
    app.static('/api', './static/api/')

    @app.route('/api/')
    async def api_index(request):
        return await response.file('./static/api/index.html')

    app.run(host="0.0.0.0", port=8080, debug=True)
