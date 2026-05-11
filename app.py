from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import webbrowser


HOST = "localhost"
PORT = 8000


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    url = f"http://{HOST}:{PORT}"
    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

    print(f"Serving Serenity Mindspace at {url}")
    print("Press Ctrl+C to stop the server.")
    webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
