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
        }
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
        }
    },
    methods: {
        onScanSuccess(decodedText, decodedResult) {
            this.$emit('result', decodedText, decodedResult);
        },

        stopScan(){
            console.log('Scanning was stopped 1');
            this.html5QrcodeScanner.stop().then((ignore) => {
                // QR Code scanning is stopped.
                console.log('Scanning was stopped');
            }).catch((err) => {
                // Stop failed, handle it.
                console.log('Error by stopping the camera');
                console.log(err)
            });
        }
    }
};
</script>
