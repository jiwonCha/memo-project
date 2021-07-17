import sys, getopt

from api import db, create_app
import api.config as config


def main(argv):
    if len(argv) == 0:
        db.create_all(app=create_app())
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
                if mode == "test" or mode == "local":
                    TEST_CONFIG = {
                        "TESTING": True,
                        "SQLALCHEMY_DATABASE_URI": config.test_db_uri(),
                    }
                    db.create_all(app=create_app(TEST_CONFIG))

    create_app().run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)


if __name__ == "__main__":
    main(sys.argv[1:])
