import dtlpy as dl


class OCR:
    def __init__(self):
        dl.use_attributes_2(state=True)

    @staticmethod
    def run(item: dl.Item):
        # construct the argument parser and parse the arguments
        annotations = item.annotations.list()
        if 'user' not in item.metadata:
            item.metadata['user'] = dict()
        buffer = item.download(save_locally=False)
        text_file_content = buffer.read().decode('utf-8')
        for annotation in annotations:
            start_idx = annotation.coordinates.get('start')
            end_idx = annotation.coordinates.get('end')
            annotation_text = text_file_content[start_idx:end_idx]
            if 'user' not in annotation.metadata:
                annotation.metadata['user'] = dict()
            annotation.metadata['user'] = {'highLightedText': annotation_text}
            annotation.update()
            item.metadata['user'][annotation.id] = {
                'annotationLabel': annotation.label,
                'highLightedText': annotation_text
            }
        item.update()
        return item
