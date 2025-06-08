from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def início():
    return render_template('Corpo.html')
#------
@app.route('/personagens')
def personagens():
    return render_template('personagens.html')
#---------
@app.route('/história')
def história():
    return render_template('história.html')
#--------
@app.route('/lendas')
def lendas():
    return render_template('lendas.html')
#---------
@app.route('/sinopse')
def sinopse():
    return render_template('sinopse.html')
#-----------
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


#---------Personagens-------------
@app.route('/elena')
def elena():
    return render_template('/personagens/Elena.html')
@app.route('/stefan')
def stefan():
    return render_template('/personagens/Stefan.html')
@app.route('/damon')
def damon():
    return render_template('/personagens/Damon.html')
@app.route('/caroline')
def caroline():
    return render_template('/personagens/Caroline.html')
@app.route('/bonnie')
def bonnie():
    return render_template('/personagens/Bonnie.html')
@app.route('/jeremy')
def jeremy():
    return render_template('/personagens/Jeremy.html')
@app.route('/matt')
def matt():
    return render_template('/personagens/Matt.html')
@app.route('/tyler')
def tyler():
    return render_template('/personagens/Tyler.html')
@app.route('/alaric')
def alaric():
    return render_template('/personagens/Alaric.html')
@app.route('/katherine')
def katherine():
    return render_template('/personagens/Katherine.html')


if __name__ == '__main__':
    app.run(debug=True)