@property
def id(self):
    if hasattr(self, 'pcGtsId'):
        return self.pcGtsId
    return self.imageFilename
