// Global placeholder variables
let trackWrapper, prevBtn, nextBtn;

// This constant is injected from Python.
const cardWidth = TOTAL_CARD_WIDTH_PLACEHOLDER;

// --- Scrolling Functions ---

function updateButtons() {
    // Look up elements again in case they weren't ready globally
    trackWrapper = document.querySelector('.card-track-wrapper');
    prevBtn = document.getElementById('prevBtn');
    nextBtn = document.getElementById('nextBtn');

    if (!trackWrapper || !prevBtn || !nextBtn) return;

    // Check if scrolled all the way left (start)
    const isAtStart = trackWrapper.scrollLeft === 0;

    // Check if scrolled all the way right (end)
    const isAtEnd = Math.ceil(trackWrapper.scrollLeft + trackWrapper.clientWidth) >= trackWrapper.scrollWidth;

    prevBtn.classList.toggle('disabled', isAtStart);
    nextBtn.classList.toggle('disabled', isAtEnd);
}

// Function called by arrow buttons to trigger native scrolling (Exposed globally)
window.slide = function(direction) {
    trackWrapper = document.querySelector('.card-track-wrapper');
    if (!trackWrapper) return;

    const scrollAmount = direction * cardWidth;

    trackWrapper.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });

    // Update buttons after a small delay to allow smooth scroll to finish
    setTimeout(updateButtons, 500);
}

// Initialize state and listeners when the window is loaded
window.onload = function() {
    // Initial element lookups
    trackWrapper = document.querySelector('.card-track-wrapper');

    if (trackWrapper) {
        // Attach scroll listener
        trackWrapper.addEventListener('scroll', updateButtons);
    }

    // Set initial button state
    updateButtons();
};