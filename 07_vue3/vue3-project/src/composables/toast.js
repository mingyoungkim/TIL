import { ref, onUnmounted } from 'vue';

export const useToast = () => {
  const showToast = ref(false); 
  const toastMsg = ref('');
  const toastAlertType = ref('');
  const toastTimeout = ref('');

  onUnmounted(() => {
    clearTimeout(timeout.value);
  });

  const triggerToast = (msg, type='succsess') => {
    showToast.value = true;
    toastMsg.value = msg;
    toastAlertType.value = type;
    toastTimeout.value = setTimeout(() => {
      showToast.value = false;
      toastAlertType.value = '';
      toastMsg.value = '';
    }, 3000);
  };
  
  return {
    showToast,
    toastMsg,
    toastAlertType,
    triggerToast,
  }
}