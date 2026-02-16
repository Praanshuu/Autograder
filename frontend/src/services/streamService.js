import { api } from './apiClient';

export const streamService = {
    // Announcements
    getAnnouncements: async (classId) => {
        try {
            const response = await api.get(`/classes/announcements/?class_id=${classId}`);
            return { success: true, data: response.data };
        } catch (error) {
            console.error("Error fetching announcements:", error);
            return { success: false, error: error.response?.data || "Failed to fetch announcements" };
        }
    },

    createAnnouncement: async (classId, data) => {
        try {
            const response = await api.post('/classes/announcements/', {
                class_obj: classId,
                content: data.content,
                is_pinned: data.is_pinned || false
            });
            return { success: true, data: response.data };
        } catch (error) {
            return { success: false, error: error.response?.data || "Failed to create announcement" };
        }
    },

    deleteAnnouncement: async (id) => {
        try {
            await api.delete(`/classes/announcements/${id}/`);
            return { success: true };
        } catch (error) {
            return { success: false, error: error.response?.data || "Failed to delete announcement" };
        }
    },

    updateAnnouncement: async (id, data) => {
        try {
            const response = await api.patch(`/classes/announcements/${id}/`, data);
            return { success: true, data: response.data };
        } catch (error) {
            return { success: false, error: error.response?.data || "Failed to update announcement" };
        }
    },

    // Comments
    // Comments
    getComments: async (announcementId, assignmentId) => {
        try {
            let url = '/classes/comments/?';
            if (announcementId) url += `announcement_id=${announcementId}`;
            if (assignmentId) url += `assignment_id=${assignmentId}`;

            const response = await api.get(url);
            return { success: true, data: response.data };
        } catch (error) {
            return { success: false, error: error.response?.data };
        }
    },

    addComment: async (data) => {
        try {
            const response = await api.post('/classes/comments/', data);
            return { success: true, data: response.data };
        } catch (error) {
            return { success: false, error: error.response?.data || "Failed to add comment" };
        }
    }
};
