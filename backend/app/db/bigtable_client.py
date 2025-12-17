from google.cloud import bigtable

class BigTableClient:
    def __init__(self, project_id, instance_id):
        self.client = bigtable.Client(project=project_id, admin=True)
        self.instance = self.client.instance(instance_id)

    def get_table(self, table_id):
        return self.instance.table(table_id)
