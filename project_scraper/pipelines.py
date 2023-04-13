
class ProjectScraperPipeline:
    def process_item(self, item, spider):
        # For another wave of parsing
        print(item)
        return item
