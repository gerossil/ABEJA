from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["solitary bee hives complete"]

for keyword in keywords:    
    response().download(keyword, 100)