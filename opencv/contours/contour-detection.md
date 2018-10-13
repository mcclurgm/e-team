# Contour Detection

Uses binary images: should convert to that first
* That can (maybe should?) be done by cv2.threshold()

## `cv2.findContours()`

[Docs](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#findcontours)

### Parameters
* image
* mode
  - Contour retrieval mode
* method

### Return
* image
* contours
  - Python list of all contours found in the image
  - Contour: Numpy array of coordinates of boundary points
* hierarchy

## `cv2.drawContours()`
### Parameters
* `image`
  - Destination image
  - Uses the pixels from this image, draws on top
* `contours`
  - Input contours you can draw
* `contourldx`
  - Select contour
  - Negative: draws all contours
* `color`
* `thickness`

### Return
* `image`
