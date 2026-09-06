// Star at Night — Creation Flow
// Manages the step-by-step gift creation experience

const STEPS = ['recipient', 'occasion', 'description', 'photo', 'tone', 'generating', 'results'];

function initCreationFlow() {
  const panel = document.querySelector('.creation-panel');
  if (!panel) return;
  
  let currentStep = 0;
  const session = window.StarAtNight.state.session;
  
  function showStep(index) {
    const steps = panel.querySelectorAll('.creation-panel__step');
    steps.forEach((step, i) => {
      step.classList.toggle('creation-panel__step--active', i === index);
    });
    currentStep = index;
  }
  
  function nextStep() {
    if (currentStep < STEPS.length - 1) {
      showStep(currentStep + 1);
    }
  }
  
  function prevStep() {
    if (currentStep > 0) {
      showStep(currentStep - 1);
    }
  }
  
  // Recipient step
  const nameInput = panel.querySelector('#recipient-name');
  const relationshipSelect = panel.querySelector('#recipient-relationship');
  
  if (nameInput) {
    nameInput.addEventListener('input', (e) => {
      session.recipient.name = e.target.value;
      window.StarAtNight.state.save();
      
      // Update dynamic text
      const dynamicName = panel.querySelector('.dynamic-name');
      if (dynamicName && e.target.value) {
        dynamicName.textContent = e.target.value;
      }
    });
  }
  
  if (relationshipSelect) {
    relationshipSelect.addEventListener('change', (e) => {
      session.recipient.relationship = e.target.value;
      window.StarAtNight.state.save();
    });
  }
  
  // Occasion chips
  const occasionChips = panel.querySelectorAll('[data-occasion]');
  occasionChips.forEach(chip => {
    chip.addEventListener('click', () => {
      occasionChips.forEach(c => c.classList.remove('chip--selected'));
      chip.classList.add('chip--selected');
      session.occasion = chip.dataset.occasion;
      window.StarAtNight.state.save();
      
      // Auto-advance after selection
      setTimeout(nextStep, 300);
    });
  });
  
  // Description textarea
  const descInput = panel.querySelector('#description');
  if (descInput) {
    descInput.addEventListener('input', (e) => {
      session.description = e.target.value;
      window.StarAtNight.state.save();
    });
  }
  
  // Add memory/joke buttons
  const addMemoryBtn = panel.querySelector('[data-action="add-memory"]');
  const addJokeBtn = panel.querySelector('[data-action="add-joke"]');
  
  if (addMemoryBtn) {
    addMemoryBtn.addEventListener('click', () => {
      const input = prompt('Add a memory:');
      if (input) {
        session.memories.push({ type: 'memory', text: input });
        window.StarAtNight.state.save();
        showToast('Memory added');
      }
    });
  }
  
  if (addJokeBtn) {
    addJokeBtn.addEventListener('click', () => {
      const input = prompt('Add an inside joke:');
      if (input) {
        session.memories.push({ type: 'joke', text: input });
        window.StarAtNight.state.save();
        showToast('Joke added');
      }
    });
  }
  
  // Tone chips
  const toneChips = panel.querySelectorAll('[data-tone]');
  toneChips.forEach(chip => {
    chip.addEventListener('click', () => {
      chip.classList.toggle('chip--selected');
      const tone = chip.dataset.tone;
      if (session.tone.includes(tone)) {
        session.tone = session.tone.filter(t => t !== tone);
      } else {
        session.tone.push(tone);
      }
      window.StarAtNight.state.save();
    });
  });
  
  // Photo upload
  const uploadArea = panel.querySelector('.upload-area');
  const fileInput = panel.querySelector('#photo-upload');
  
  if (uploadArea && fileInput) {
    uploadArea.addEventListener('click', () => fileInput.click());
    
    uploadArea.addEventListener('dragover', (e) => {
      e.preventDefault();
      uploadArea.classList.add('upload-area--dragover');
    });
    
    uploadArea.addEventListener('dragleave', () => {
      uploadArea.classList.remove('upload-area--dragover');
    });
    
    uploadArea.addEventListener('drop', (e) => {
      e.preventDefault();
      uploadArea.classList.remove('upload-area--dragover');
      handleFiles(e.dataTransfer.files);
    });
    
    fileInput.addEventListener('change', (e) => {
      handleFiles(e.target.files);
    });
  }
  
  function handleFiles(files) {
    for (const file of files) {
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
          session.photos.push({
            name: file.name,
            data: e.target.result
          });
          window.StarAtNight.state.save();
          showToast('Photo added');
          
          // Show preview
          const preview = uploadArea.querySelector('.upload-preview');
          if (preview) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.className = 'upload-preview__img';
            preview.appendChild(img);
          }
        };
        reader.readAsDataURL(file);
      }
    }
  }
  
  // Navigation buttons
  const nextBtns = panel.querySelectorAll('[data-action="next"]');
  const prevBtns = panel.querySelectorAll('[data-action="prev"]');
  const submitBtn = panel.querySelector('[data-action="submit"]');
  
  nextBtns.forEach(btn => btn.addEventListener('click', nextStep));
  prevBtns.forEach(btn => btn.addEventListener('click', prevStep));
  
  if (submitBtn) {
    submitBtn.addEventListener('click', () => {
      showStep(STEPS.indexOf('generating'));
      simulateGeneration();
    });
  }
  
  // Open/close panel
  const openBtns = document.querySelectorAll('[data-action="open-creation"]');
  openBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      panel.classList.add('creation-panel--open');
      showStep(0);
    });
  });
  
  const closeBtn = panel.querySelector('[data-action="close"]');
  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      panel.classList.remove('creation-panel--open');
    });
  }
  
  // Simulate AI generation
  function simulateGeneration() {
    const loadingTexts = [
      `Thinking about ${session.recipient.name || 'them'}...`,
      'Finding the detail that makes this hers...',
      'Sketching a few directions...',
      'Putting the finishing touches on them...'
    ];
    
    const textEl = panel.querySelector('.loading__text');
    let i = 0;
    
    const interval = setInterval(() => {
      if (i < loadingTexts.length) {
        textEl.textContent = loadingTexts[i];
        i++;
      } else {
        clearInterval(interval);
        showStep(STEPS.indexOf('results'));
        showResults();
      }
    }, 800);
  }
  
  function showResults() {
    const name = session.recipient.name || 'someone';
    const resultsHeader = panel.querySelector('.results-header');
    if (resultsHeader) {
      resultsHeader.textContent = `I made three things for ${name}.`;
    }
    
    // Show staggered results
    const cards = panel.querySelectorAll('.product-card');
    cards.forEach((card, i) => {
      card.style.animationDelay = `${i * 90}ms`;
      card.classList.add('animate-fade-in-up');
    });
  }
  
  // Initialize
  showStep(0);
}

// Toast utility
function showToast(message) {
  const toast = document.querySelector('.toast');
  if (toast) {
    toast.textContent = message;
    toast.classList.add('toast--visible');
    setTimeout(() => {
      toast.classList.remove('toast--visible');
    }, 2000);
  }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', initCreationFlow);

window.StarAtNight = window.StarAtNight || {};
window.StarAtNight.creationFlow = { init: initCreationFlow };
