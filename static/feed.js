
    console.log("Hello ")
    function toggleLike(icon) {
        icon.classList.toggle('fas'); // Toggle filled heart
        icon.classList.toggle('far'); // Toggle empty heart
        
    }

    function toggleCommentSection(icon) {
        const post = icon.closest('.post');
        const commentSection = post.querySelector('.comment-section');
        commentSection.style.display = commentSection.style.display === 'none' ? 'block' : 'none';
    }

    function addComment(button) {
        const post = button.closest('.post');
        const commentInput = post.querySelector('.comment-input');
        const commentsSection = post.querySelector('.comment-section');

        if (commentInput.value.trim() !== '') {
            const newComment = document.createElement('div');
            newComment.classList.add('comment');
            newComment.innerHTML = `<span class="username">You:</span> ${commentInput.value}`;
            commentsSection.appendChild(newComment);
            commentInput.value = '';
        }
    }