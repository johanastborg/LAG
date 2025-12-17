from google.cloud import spanner

class SpannerClient:
    def __init__(self, project_id, instance_id, database_id):
        self.client = spanner.Client(project=project_id)
        self.instance = self.client.instance(instance_id)
        self.database = self.instance.database(database_id)

    def execute_query(self, query, params=None):
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql(query, params=params)
            return list(results)
