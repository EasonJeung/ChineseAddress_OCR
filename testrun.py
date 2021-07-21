from demo_final import demo_flask
image_file="./demo.png" # image path
output_file,ret_total = demo_flask(image_file)
print('Recognition Result:')
print(ret_total)
