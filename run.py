from project import create_app

app = create_app('default') 

if __name__ == '__main__':
    app.run(port=8080,debug=True)