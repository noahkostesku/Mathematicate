// Importing the 3D Model

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });

const container = document.querySelector('.ThreeDContainer');
const containerWidth = container.clientWidth;
const containerHeight = container.clientHeight;

renderer.setSize(containerWidth, containerHeight);
container.appendChild(renderer.domElement);

const hlight = new THREE.AmbientLight(0xffffff, 100);
scene.add(hlight);

const dlight = new THREE.DirectionalLight(0xffffff, 100);
dlight.position.set(10, 10, 10);
scene.add(dlight);

const loader = new GLTFLoader();
let model;


loader.load('torus.glb', function (gltf) {
    model = gltf.scene;
    model.scale.set(4, 5, 4); 
    model.position.set(0, -4, 0);
    scene.add(model);
}, undefined, function (error) {
    console.error(error);
});

const controls = new OrbitControls(camera, renderer.domElement);
camera.position.set(0, 2, 5);

function animate() {
    requestAnimationFrame(animate);
    
    if (model) {
        model.rotation.y += 0.005;
    }
    
    controls.update();
    renderer.render(scene, camera);
}

animate();

//for resonsive browser resizing

window.addEventListener('resize', () => {
    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;
    
    camera.aspect = containerWidth / containerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(containerWidth, containerHeight);
});