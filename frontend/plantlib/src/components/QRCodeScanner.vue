<template>
    <div id="qr-code-full-region"></div>
</template>

<script>
import {Html5QrcodeScanner} from "html5-qrcode"


export default {
    props: {
        qrbox: {
            type: Number,
            default: 250
        },
        fps: {
            type: Number,
            default: 10
        },
        stop: {
            type: Boolean,
            default: false
        },
        autoStop: {
            type: Boolean,
            default: false
        },
    },
    mounted() {
        const config = {
            fps: this.fps,
            qrbox: this.qrbox,
        };
        const html5QrcodeScanner = new Html5QrcodeScanner('qr-code-full-region', config);
        html5QrcodeScanner.render(this.onScanSuccess);
        this.html5QrcodeScanner = html5QrcodeScanner;
    },
    watch: {
        stop(){
            this.stopScan()
        },
        autoStop(){
            this.stopScan()
        },
    },
    methods: {
        onScanSuccess(decodedText, decodedResult) {
            this.$emit('result', decodedText, decodedResult);
        },

        stopScan(){
            console.log('Scanning was stopped 1');
            this.html5QrcodeScanner.clear()
        }
    }
};
</script>
