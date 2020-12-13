<<<<<<< HEAD
const video = document.getElementById('video')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    {video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    detectedExpressions = detections[0].expressions;
    console.log(detections);
    // console.log(detectedExpressions);
    // console.log("neutral " + detectedExpressions.neutral);
    // console.log("happy " + detectedExpressions.happy);
    // console.log("sad " + detectedExpressions.sad);
    // console.log("disgusted " + detectedExpressions.disgusted);
    // console.log("angry " + detectedExpressions.angry);
    // console.log("fearful " + detectedExpressions.fearful);
    // console.log("surprise " + detectedExpressions.surprise);
    console.log(closest(detectedExpressions,1));
  
  }, 100)
})

function closest(array,num){
  var i = 0;
  var minDiff = 1000;
  var ans;
  for(i in array){
    var m=Math.abs(num-array[i]);
    if(m<minDiff){ 
      minDiff=m; 
      ans=array[i];   
      index = i;
    }
  }
  return index;
}
=======
const video = document.getElementById("video");

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri("/models"),
  faceapi.nets.faceLandmark68Net.loadFromUri("/models"),
  faceapi.nets.faceRecognitionNet.loadFromUri("/models"),
  faceapi.nets.faceExpressionNet.loadFromUri("/models"),
  faceapi.nets.ageGenderNet.loadFromUri("/models")
]).then(startVideo);

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => (video.srcObject = stream),
    err => console.error(err)
  );
}

// video.addEventListener('play', () => {
//   // making our canvas
//   const canvas = faceapi.createCanvasFromMedia(video);
//   document.body.append(canvas);

//   // sizing our canvas
//   const displaySize = { width: video.width, height: video.height }
//   faceapi.matchDimensions(canvas, displaySize)


//   setInterval(async () => {
//     const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions());
//     const resizedDetections = faceapi.resizeResults(detections, displaySize)

//     faceapi.draw.drawDetections(canvas, resizedDetections);
//     faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
//     faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
//   }, 100);
// })

>>>>>>> AJ
