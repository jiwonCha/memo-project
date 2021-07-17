import sys, getopt

from api import db, create_app


def main(argv):
    if len(argv) == 0:
        app = create_app()
    else:
        try:
            opts, args = getopt.getopt(argv, "hm:")
        except getopt.GetoptError:
            print("main.py -m <execute_mode>")
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-h":
                print("main.py -m <execute_mode>")
                sys.exit(2)
            elif opt == "-m":
                mode = arg
                if mode == "local":
                    TEST_CONFIG = {
                        "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:',
                    }
                    db.create_all(app=create_app(TEST_CONFIG))

                    app = create_app(TEST_CONFIG)
    
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)


if __name__ == "__main__":
    main(sys.argv[1:])
