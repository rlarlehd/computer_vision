import cv2

img = cv2.imread('lena.png')
img_canvas = img.copy()

drawing = False
ix, iy = -1, -1
shape_type = 0

def draw(event, x, y, flags, param):
    global drawing, ix, iy, shape_type, img_canvas
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_temp = img_canvas.copy()
            if shape_type == 0:
                cv2.rectangle(img_temp, (ix, iy), (x, y), (0, 255, 0), 2)
            elif shape_type == 1:
                cv2.line(img_temp, (ix, iy), (x, y), (0, 0, 255), 2)
            elif shape_type == 2:
                cv2.arrowedLine(img_temp, (ix, iy), (x, y), (255, 0, 0), 2)
            
            cv2.imshow('Drawing', img_temp)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if shape_type == 0:
            cv2.rectangle(img_canvas, (ix, iy), (x, y), (0, 255, 0), 2)
        elif shape_type == 1:
            cv2.line(img_canvas, (ix, iy), (x, y), (0, 0, 255), 2)
        elif shape_type == 2:
            cv2.arrowedLine(img_canvas, (ix, iy), (x, y), (255, 0, 0), 2)
        
        cv2.imshow('Drawing', img_canvas)

cv2.namedWindow('Drawing')
cv2.setMouseCallback('Drawing', draw)

cv2.imshow('Drawing', img_canvas)

while True:
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('r'):
        shape_type = 0
    elif key == ord('l'):
        shape_type = 1
    elif key == ord('a'):
        shape_type = 2
    elif key == ord('w'):
        cv2.imwrite('lena_2.png', img_canvas)
        print("lena_2.png")
    elif key == ord('c'):
        img_canvas = img.copy()
        cv2.imshow('Drawing', img_canvas)
    elif key == 27:
        break

cv2.destroyAllWindows()