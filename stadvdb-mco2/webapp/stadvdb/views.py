from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json

@csrf_exempt
def index(request):
    if request.method == 'GET':
        # Render the HTML template
        return render(request, 'stadvdb/index.html')  # Ensure `index.html` exists in the templates directory

    if request.method == 'POST':
        try:
            # Parse the incoming request body
            data = json.loads(request.body)
            query = data.get('query')

            if not query:
                return JsonResponse({'message': 'Query is required'}, status=400)

            # Execute the query using Django's database connection
            with connection.cursor() as cursor:
                cursor.execute(query)
                if cursor.description:  # If query returns data (e.g., SELECT)
                    columns = [col[0] for col in cursor.description]
                    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                else:  # For non-SELECT queries
                    connection.commit()
                    results = {'message': 'Query executed successfully'}

            return JsonResponse(results, safe=False)

        except Exception as e:
            # Log the error to the console for debugging
            print(f"Error executing query: {str(e)}")
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)