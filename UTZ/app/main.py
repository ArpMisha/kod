from app import app
import view 
from kks.blueprint import kks
from asutp.blueprint import asutp

app.register_blueprint(kks)
app.register_blueprint(asutp)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')

