from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ホームページ</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
            }
            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin: 20px;
            }
            .card {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 8px;
                width: 250px;
                margin: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.2s ease-in-out;
            }
            .card:hover {
                transform: translateY(-5px);
            }
            .card h2 {
                font-size: 18px;
                margin: 20px 0 10px 0;
            }
            .card a {
                text-decoration: none;
                color: #007BFF;
                font-weight: bold;
                display: block;
                margin: 10px 0;
                padding: 10px;
                border-radius: 4px;
                background-color: #f4f4f9;
                transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
            }
            .card a:hover {
                background-color: #007BFF;
                color: #fff;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align: center; margin: 20px 0;">Welcome to the Home Page</h1>
        <div class="container">
            <div class="card">
                <h2>勤務簿</h2>
                <a href="/attendance/calendar/">Go to 勤務簿</a>
            </div>
            <div class="card">
                <h2>ユーザ登録</h2>
                <a href="/accounts/register/">Register User</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
