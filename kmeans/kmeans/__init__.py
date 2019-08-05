from flask import Flask, render_template, request, jsonify
import kmeans.k_means_alg


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/kmean', methods=['POST'])
def kmean():
    clusters_number = request.form['number']
    if clusters_number:
        if not str.isdigit(clusters_number):
            return jsonify({'error': 'Please insert a number'})
        else:
            result_path = k_means_alg.run_algorithm(int(clusters_number))
            return jsonify(result_path)

    return jsonify({'error': 'Please insert a number'})


if __name__ == '__main__':
    app.run()
