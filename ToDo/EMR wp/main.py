from website import create_ws_app

app = create_ws_app()

if __name__ == "__main__":
    app.run(debug=True)