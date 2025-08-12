# Overview

This is a voice-based English practice application that allows users to engage in different types of conversational practice sessions. The app uses React for the frontend, Express.js for the backend, and integrates with OpenAI for AI-powered conversations. Users can start practice sessions with keywords across different practice types (conversation, business, storytelling, presentation), engage in real-time voice interactions, and track their practice history with quality assessments.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: React 18+ with TypeScript using Vite as the build tool
- **UI Library**: shadcn/ui components built on Radix UI primitives with Tailwind CSS for styling
- **State Management**: TanStack Query (React Query) for server state management and caching
- **Routing**: Wouter for client-side routing (lightweight alternative to React Router)
- **Voice Integration**: Web Speech API through custom React hooks for speech recognition and synthesis
- **Form Handling**: React Hook Form with Zod validation for type-safe form management

## Backend Architecture
- **Framework**: Express.js with TypeScript running in ESM mode
- **API Design**: RESTful API structure with dedicated route handlers
- **Database Layer**: Drizzle ORM for type-safe database operations with PostgreSQL dialect
- **Storage Pattern**: Abstract storage interface (IStorage) with in-memory implementation for development
- **Error Handling**: Centralized error handling middleware with structured error responses
- **Development Tools**: Hot module replacement with Vite integration for seamless development experience

## Data Storage Solutions
- **Database**: PostgreSQL configured through Drizzle ORM with schema-first approach
- **Schema Design**: Two main entities - practice sessions and conversation messages with proper relationships
- **Migration System**: Drizzle Kit for database migrations and schema synchronization
- **Development Storage**: In-memory storage implementation for rapid prototyping and testing

## Authentication and Authorization
- **Current State**: No authentication system implemented
- **Session Management**: Practice sessions are identified by UUID but not tied to user accounts
- **Access Control**: Open access to all endpoints without authorization checks

## Voice Processing System
- **Speech Recognition**: Browser's native Web Speech API for converting speech to text
- **Speech Synthesis**: Web Speech Synthesis API for text-to-speech functionality
- **Audio State Management**: Custom React hooks managing listening, processing, and speaking states
- **Language Support**: Configured for English language recognition and synthesis

## Real-time Features
- **Voice Interface**: Real-time speech recognition and synthesis for natural conversation flow
- **State Synchronization**: Immediate UI updates reflecting conversation state changes
- **Error Handling**: Graceful degradation when speech APIs are unavailable

# External Dependencies

## AI Services
- **Gemini API**: Google's Gemini AI integration for generating short, conversational responses (maximum 15 words per response)
- **Configuration**: Environment variable-based API key management (GEMINI_API_KEY) with fallback handling
- **Response Style**: Optimized for natural dialogue flow with brief responses and simple questions

## Database Services
- **Neon Database**: Serverless PostgreSQL provider configured through DATABASE_URL environment variable
- **Connection Management**: Managed through @neondatabase/serverless driver for optimal performance

## UI and Styling
- **Tailwind CSS**: Utility-first CSS framework with custom design system variables
- **Radix UI**: Headless UI components providing accessibility and interaction primitives
- **Lucide Icons**: Consistent icon set throughout the application interface

## Development Tools
- **Replit Integration**: Custom plugins for development environment optimization and error overlay
- **Build Pipeline**: Vite for frontend bundling and esbuild for server-side compilation
- **Type Safety**: Comprehensive TypeScript configuration with path mapping and strict type checking

## Third-party Libraries
- **TanStack Query**: Server state management, caching, and synchronization
- **React Hook Form**: Form state management with validation integration
- **Zod**: Runtime type validation and schema definition
- **Date-fns**: Date manipulation and formatting utilities
- **Class Variance Authority**: Type-safe CSS class composition for component variants