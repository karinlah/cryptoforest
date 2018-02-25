from flask import Flask, render_template, request

# TODO fill the api
# url_api = 'YOUR_API_ADDRESS'
application = Flask(__name__)
application.debug = True
application.secret_key = 'KukuPineapple'


@application.route('/')
def main(done=False):
    return render_template('index.html', done=done)


@application.route('/send_signal', methods=['POST'])
def send_signal():
    form_j = request.form.to_dict()

    # in case it's BTC matket, convert the sat to BTC
    if form_j.get('market') == 'BTC':
        form_j['ep_low'] = float(form_j.get('ep_low')) / (100000)
        form_j['ep_high'] = float(form_j.get('ep_high')) / (100000)

    # TODO uncomment and
    # r = requests.post(url_api, data=form_j)

    return main(done=True)


if __name__ == '__main__':
    application.run()
